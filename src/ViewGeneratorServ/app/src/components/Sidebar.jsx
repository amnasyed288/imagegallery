import React from 'react';
import './Sidebar.css'; // You can create a separate CSS file for styling

const Sidebar = () => {
  return (
    <div className="sidebar">
      {/* Your components go here */}
      <div className="sidebar-component">
        <h3>Component 1</h3>
        {/* Add your component content here */}
      </div>
      <div className="sidebar-component">
        <h3>Component 2</h3>
        {/* Add your component content here */}
      </div>
      {/* Add more components as needed */}
    </div>
  );
};

export default Sidebar;