import React from 'react';

const Footer = () => {
  return (
    <footer className="bg-purple-800 text-white py-6">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row justify-between items-center">
          <div className="mb-4 md:mb-0">
            <h3 className="text-xl font-bold">FairyAsle</h3>
            <p className="text-purple-200 mt-1">AI-Powered Fairytales for Kids</p>
          </div>
          
          <div className="text-center md:text-right">
            <p className="text-purple-200">© {new Date().getFullYear()} FairyAsle. All rights reserved.</p>
            <p className="text-purple-300 mt-1">Made with ❤️ for children everywhere</p>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer; 