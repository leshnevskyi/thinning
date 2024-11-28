import {
  FileUploadDropzone,
  FileUploadRoot,
} from "@/components/ui/file-upload";
import { Image, Box, Flex, Heading } from "@chakra-ui/react";
import { useState } from "react";

function App() {
  const [originalImageSource, setOriginalImageSource] = useState<string>();
  const [thinnedImageSource, setThinnedImageSource] = useState<string>();

  return (
    <Flex padding={5} height="100vh" flexDirection="column" gap={5}>
      {thinnedImageSource && originalImageSource && (
        <Flex height="full" width="full" overflow="hidden" gap={5}>
          <Flex flex={1} flexDirection="column" gap={3}>
            <Heading>Original image</Heading>
            <Image
              src={originalImageSource}
              alt="Original image"
              height="full"
              width="full"
              fit="contain"
            />
          </Flex>
          <Flex flex={1} flexDirection="column" gap={3}>
            <Heading>Thinned image</Heading>
            <Image
              src={thinnedImageSource}
              alt="Thinned image"
              height="full"
              width="full"
              fit="contain"
            />
          </Flex>
        </Flex>
      )}
      <Box height={thinnedImageSource ? 40 : "full"}>
        <FileUploadRoot
          width="full"
          height="full"
          alignItems="stretch"
          accept={["image/png", "image/jpeg", "image/jpg"]}
          onFileAccept={async (details) => {
            const formData = new FormData();
            const file = details.files[0];
            formData.append("file", file);

            try {
              const response = await fetch(
                "http://localhost:8000/image-thinning",
                {
                  method: "POST",
                  body: formData,
                }
              );

              if (!response.ok)
                throw new Error(
                  `Failed to process the image. Server response: ${await response.text()}`
                );

              const reader = new FileReader();

              reader.onload = (event) => {
                const result = event.target?.result;

                if (typeof result == "string") setOriginalImageSource(result);
              };

              reader.readAsDataURL(file);

              const url = URL.createObjectURL(await response.blob());
              setThinnedImageSource(url);
            } catch (error) {
              console.error(error);
            }
          }}
        >
          <FileUploadDropzone
            height="full"
            minHeight={0}
            label="Drag and drop here to upload"
            description=".png, .jpg, .jpeg"
            rounded={20}
            borderColor="gray.300"
          />
        </FileUploadRoot>
      </Box>
    </Flex>
  );
}

export default App;
