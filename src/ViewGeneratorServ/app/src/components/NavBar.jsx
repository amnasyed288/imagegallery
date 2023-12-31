import { NavLink } from "react-router-dom";
import "./NavBar.css";

function NavBar({ isLoggedIn, setIsLoggedIn }) {
  const logoutHandler = () => setIsLoggedIn(false)

  return (
    <>
      <nav className="navbar">
        <div className="nav-container">
          <NavLink exact to="/" className="nav-logo">
            <span>Gallery</span>
          </NavLink>

          <ul className={"nav-menu"}>

            {
              isLoggedIn ? (
                <>
                  <li className="nav-item">
                    <NavLink exact='true' to="/Gallery" className="nav-links" >
                      Home
                    </NavLink>
                  </li>
                  <li className="nav-item">
                    <NavLink exact='true' to="/Login" className="nav-links" onClick={logoutHandler}>
                      Logout
                    </NavLink>
                  </li>

                </>
              ) : null
            }
            {
              !isLoggedIn ? (
                <>
                  <li className="nav-item">
                    <NavLink exact to="/Login" className="nav-links" >
                      Log In
                    </NavLink>
                  </li>
                  <li className="nav-item">
                    <NavLink exact to="/Register" className="nav-links" >
                      Register
                    </NavLink>
                  </li>
                </>
              ) : null
            }

          </ul>

        </div>
      </nav>
    </>
  );
}

export default NavBar;
