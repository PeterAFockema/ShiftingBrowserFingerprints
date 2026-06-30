const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const artifactsDir = path.join(__dirname, 'web-ext-artifacts');

try {
  // Step 1: Run the official web-ext build tool
  console.log('Building package via web-ext...');
  execSync('npx web-ext build --overwrite-dest', { stdio: 'inherit' });

  // Step 2: Locate the freshly built .zip file
  const files = fs.readdirSync(artifactsDir);
  const zipFile = files.find(file => file.endsWith('.zip'));

  if (!zipFile) {
    throw new Error('No .zip archive was found inside web-ext-artifacts/.');
  }

  // Step 3: Explicitly rename the .zip extension to .xpi
  const oldPath = path.join(artifactsDir, zipFile);
  const newPath = path.join(artifactsDir, zipFile.replace('.zip', '.xpi'));

  // Clear an old xpi if it exists so Windows/Linux doesn't throw a lock error
  if (fs.existsSync(newPath)) fs.unlinkSync(newPath);

  fs.renameSync(oldPath, newPath);
  console.log(`\n🎉 Success! Created: ./web-ext-artifacts/${zipFile.replace('.zip', '.xpi')}`);

} catch (error) {
  console.error('\nBuild step failed:', error.message);
  process.exit(1);
}