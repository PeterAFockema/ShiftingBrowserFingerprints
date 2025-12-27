{
    const image_data = CanvasRenderingContext2D.prototype.getImageData;

    const randomise = function(canvas, context) {
        if (context) {
            
            const canvas_width = canvas.width
            const canvas_height = canvas.height

            if (canvas_width && canvas_height) {
                const updated_image_data = image_data.apply(context, [0, 0, canvas_width, canvas_height]);
                //TODO: Add updates to randomise the image data here
                window.postMessage("canvas_intercept", "*");
                context.putImageData(updated_image_data, 0, 0); 
                //The CanvasRenderingContext2D.putImageData() method of the Canvas 2D API paints 
                // data from the given ImageData object onto the canvas
            }

        }
    };

    HTMLCanvasElement.prototype.toBlob = new Proxy(HTMLCanvasElement.prototype.toBlob, {
        apply(target, self, args) {
            randomise(self, self.getContext("2d"));
            return Reflect.apply(target, self, args);
        }
    });

    HTMLCanvasElement.prototype.toDataURL = new Proxy(HTMLCanvasElement.prototype.toDataURL, {
        apply(target, self, args) {
            randomise(self, self.getContext("2d"));
            return Reflect.apply(target, self, args);
        }
    });

    CanvasRenderingContext2D.prototype.getImageData = new Proxy(CanvasRenderingContext2D.prototype.getImageData, {
        apply(target, self, args) {
            randomise(self.canvas, self);
            return Reflect.apply(target, self, args);
        }
    });   
}