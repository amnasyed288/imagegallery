import React, { useState } from 'react';
import ImageUploading from 'react-images-uploading';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Sidebar from '../Sidebar';

const Gallery = ({ userId }) => {
  const [images, setImages] = useState([]);
  const [uploadedImageUrls, setUploadedImageUrls] = useState([]);
  const maxNumber = 69;

  const onChange = (imageList) => {
    setImages(imageList);
  };


  const onImageUploadB = async () => {
    const formData = new FormData();
    images.forEach((image, index) => {
      formData.append(`image${index + 1}`, image.file, userId);
      // console.log("DATA: " + formData)
    });

    try {
      // Adjust the URL to match your backend endpoint
      const response = await axios.post('http://localhost:5000/upload', formData, {
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
        <h1 className='text-center'>Upload Images</h1>
        <ImageUploading multiple value={images} onChange={onChange} maxNumber={maxNumber} dataURLKey="data_url">
          {({ imageList, onImageUpload, onImageUpdate, onImageRemove }) => (
            <div className='text-center mt-3'>
              <button className='btn btn-primary mx-2' onClick={onImageUpload}>Upload Image</button>
              <button className='btn btn-primary' onClick={onImageUploadB}>Upload to Backend</button>
              {uploadedImageUrls.map((imageUrl, index) => (
                <div key={index} >
                  <img src={imageUrl} alt="" width="100" />
                </div>
              ))}
              {imageList.map((image, index) => (
                <div key={index} style={{ marginBottom: '10px' }}>
                  <img className='mt-3 border border-4 border-danger' src={image['data_url']} alt="" width="500" />
                  <div className='my-5'>
                    <button className='btn btn-info mx-5' onClick={() => onImageUpdate(index)}>Update</button>
                    <button className='btn btn-danger' onClick={() => onImageRemove(index)}>Remove</button>
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
