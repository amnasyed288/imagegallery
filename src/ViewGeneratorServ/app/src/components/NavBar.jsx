import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import "./NavBar.css";

function NavBar() {
  const [click, setClick] = useState(false);

  const handleClick = () => setClick(!click);

  return (
    <>
      <nav className="navbar">
        <div className="nav-container">
          <NavLink exact to="/" className="nav-logo">
            <span>Gallery</span>
          </NavLink>

          <ul className={click ? "nav-menu active" : "nav-menu"}>
            <li className="nav-item">
              <NavLink
                exact
                to="/Gallery"
                
                className="nav-links"
                onClick={handleClick}
              >
                Home
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                exact
                to="/Login"
                
                className="nav-links"
                onClick={handleClick}
              >
                Log In
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                exact
                to="/Register"
                
                className="nav-links"
                onClick={handleClick}
              >
                Register
              </NavLink>
            </li>
            
          </ul>
          <div className="nav-icon" onClick={handleClick}>
            {/* Remove or comment out the icon-related code */}
          </div>
        </div>
      </nav>
    </>
  );
}

export default NavBar;
