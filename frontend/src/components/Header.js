import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="bg-gradient-to-r from-pink-400 to-purple-500 shadow-md">
      <div className="container mx-auto px-4 py-3 flex justify-between items-center">
        <Link to="/" className="flex items-center">
         {/* <img src={logo} alt="FairyAsle" className="h-12 mr-3" /> */}
          <span className="text-2xl font-bold text-white font-display">FairyAsle</span>
        </Link>
        <nav>
          <ul className="flex space-x-6">
            <li>
              <Link to="/" className="text-white hover:text-yellow-200 font-medium text-lg transition-colors">
                Home
              </Link>
            </li>
            <li>
              <Link to="/create" className="bg-yellow-400 hover:bg-yellow-300 text-purple-800 font-bold py-2 px-4 rounded-full shadow-md transition-colors">
                Create Story
              </Link>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header; 