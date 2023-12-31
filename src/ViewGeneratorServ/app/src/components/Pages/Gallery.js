import React, { useState } from 'react';
import ImageUploading from 'react-images-uploading';
import axios from 'axios';
import Sidebar from '../Sidebar';

const Gallery = () => {
  const [images, setImages] = useState([]);
  const [uploadedImageUrls, setUploadedImageUrls] = useState([]);
  const maxNumber = 69;

  const onChange = (imageList, addUpdateIndex) => {
    setImages(imageList);
  };

  const onImageUploadB = async () => {
    const formData = new FormData();
    images.forEach((image, index) => {
      formData.append(`image${index + 1}`, image.file);
    });

    try {
      // Adjust the URL to match your backend endpoint
      const response = await axios.post('http://localhost:5001/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      console.log('Upload successful:', response.data);

      // Update state with the uploaded image URLs
      setUploadedImageUrls(response.data.imageUrls);
    } catch (error) {
      console.error('Error during upload:', error.message);
      // Handle error as needed
    }
  };

  return (
    <>
      {/* <Sidebar /> */}
      <div>
        <h1>Upload Images</h1>
        <ImageUploading multiple value={images} onChange={onChange} maxNumber={maxNumber} dataURLKey="data_url"
        >
          {({ imageList, onImageUpload, onImageUpdate, onImageRemove }) => (
            <div>
              <button onClick={onImageUpload}>Upload Image</button>
              <button onClick={onImageUploadB}>Upload to Backend</button>
              {uploadedImageUrls.map((imageUrl, index) => (
                <div key={index} style={{ marginBottom: '10px' }}>
                  <img src={imageUrl} alt="" width="100" />
                </div>
              ))}
              {imageList.map((image, index) => (
                <div key={index} style={{ marginBottom: '10px' }}>
                  <img src={image['data_url']} alt="" width="100" />
                  <div>
                    <button onClick={() => onImageUpdate(index)}>Update</button>
                    <button onClick={() => onImageRemove(index)}>Remove</button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </ImageUploading>
      </div>
    </>
  );
};

export default Gallery;
