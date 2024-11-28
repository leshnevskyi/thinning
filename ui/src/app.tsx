import {
  FileUploadDropzone,
  FileUploadRoot,
} from "@/components/ui/file-upload";
import { useState } from "react";

function App() {
  const [thinnedImageSource, setThinnedImageSource] = useState<string>();

  return (
    <>
      <FileUploadRoot
        maxW="xl"
        alignItems="stretch"
        onFileAccept={async (details) => {
          const formData = new FormData();
          formData.append("file", details.files[0]);

          try {
            const response = await fetch(
              "http://localhost:8000/image-thinning",
              {
                method: "POST",
                body: formData,
              }
            );

            if (!response.ok) throw new Error("Failed to process the image.");

            const blob = await response.blob();
            const url = URL.createObjectURL(blob);
            console.log(url);
            setThinnedImageSource(url);
          } catch (error) {
            console.error(error);
            alert("Error processing image.");
          }
        }}
      >
        <FileUploadDropzone
          label="Drag and drop here to upload"
          description=".png, .jpg up to 5MB"
        />
      </FileUploadRoot>
      {thinnedImageSource && (
        <img src={thinnedImageSource} alt="Processed image" />
      )}
    </>
  );
}

export default App;
