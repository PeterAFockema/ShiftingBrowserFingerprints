import io
import sys
import subprocess
import unittest

import shiftingbrowserfingerprints.generate_xpis as generation_of_xpis

class TestBuildExtension(unittest.TestCase):

    def setUp(self):
        self.original_run = subprocess.run
        self.original_stdout = sys.stdout

        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

        self.called_command = None
        self.called_kwargs = None

    def tearDown(self):
        subprocess.run = self.original_run
        sys.stdout = self.original_stdout

    def fake_run(self, command, **kwargs):
        self.called_command = command
        self.called_kwargs = kwargs

        class FakeResult:
            stdout = "web-ext success output"

        return FakeResult()

    def fake_function_that_raises_error(self, command, **kwargs):
                raise subprocess.CalledProcessError(
                    returncode=1, cmd=command, stderr="Error: missing manifest"
                ) 
    
    def test_build_extension_success(self):
        subprocess.run = self.fake_run

        generation_of_xpis.build_extension("/workspace/project", "fake-addon")

        self.assertIn("web-ext", self.called_command)
        self.assertIn(
            "/workspace/project/__assets__/extensions/fake-addon",
            self.called_command,
        )
        self.assertEqual(self.called_kwargs.get("shell"), True)

        printed_text = self.captured_output.getvalue()
        self.assertIn("Build successful for fake-addon!", printed_text)
        self.assertIn("web-ext success output", printed_text)

    def test_build_extension_failure_exceptions_are_caught(self):

        subprocess.run = self.fake_function_that_raises_error
        generation_of_xpis.build_extension("/workspace/project", "broken-addon")

        printed_text = self.captured_output.getvalue()

        self.assertIn("Build failed for broken-addon!", printed_text)
        self.assertIn("Error: missing manifest", printed_text)

    def test_windows_path_backslashes_correctly_convert(self):

        subprocess.run = self.fake_run

        generation_of_xpis.build_extension(
            r"C:\Users\Dev\Project", "win-addon"
        ) # This uses a Windows path string

        source_dir_index = self.called_command.index("--source-dir") + 1
        actual_source_dir = self.called_command[source_dir_index]

        self.assertNotIn("\\", actual_source_dir)
        self.assertEqual(
            actual_source_dir,
            "C:/Users/Dev/Project/__assets__/extensions/win-addon",
        )

if __name__ == "__main__":
    unittest.main()
