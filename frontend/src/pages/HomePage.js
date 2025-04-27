import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div className="max-w-6xl mx-auto">
      <div className="flex flex-col md:flex-row items-center justify-between py-12">
        <div className="md:w-1/2 mb-10 md:mb-0">
          <h1 className="text-4xl md:text-5xl font-bold text-purple-800 mb-6">
            Magical Stories for <span className="text-pink-500"> Kids</span>
          </h1>
          <p className="text-xl text-gray-700 mb-8">
          FairyAsle invites children to use their imagination to create magical fairytales that inspire comfort, courage, and emotional growth.
          </p>
          <div className="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4">
            <Link 
              to="/create" 
              className="bg-gradient-to-r from-purple-600 to-pink-500 hover:from-purple-700 hover:to-pink-600 text-white font-bold py-3 px-8 rounded-full shadow-lg transform transition-all duration-300 hover:scale-105 text-center"
            >
              Create Your Story
            </Link>
            <a 
              href="#how-it-works" 
              className="bg-white text-purple-700 border-2 border-purple-500 font-bold py-3 px-8 rounded-full shadow-md hover:bg-purple-50 transition-colors text-center"
            >
              Learn More
            </a>
          </div>
        </div>
        <div className="md:w-1/2 ml-10">
          <img 
            src="images/home-image.jpeg" 
            alt="Children reading magical stories" 
            className="w-70 h-auto rounded-2xl shadow-xl animate-float"
          />
        </div>
      </div>

      <div id="how-it-works" className="py-16">
        <h2 className="text-3xl font-bold text-center text-purple-800 mb-12">How It Works</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="bg-white p-6 rounded-xl shadow-md">
            <div className="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mb-4 mx-auto">
              <span className="text-2xl font-bold text-purple-600">1</span>
            </div>
            <h3 className="text-xl font-bold text-center text-purple-700 mb-3">Share Your Story Idea</h3>
            <p className="text-gray-600 text-center">
              Tell us what your story should be about. Add images if you'd like!
            </p>
          </div>
          
          <div className="bg-white p-6 rounded-xl shadow-md">
            <div className="w-16 h-16 bg-pink-100 rounded-full flex items-center justify-center mb-4 mx-auto">
              <span className="text-2xl font-bold text-pink-600">2</span>
            </div>
            <h3 className="text-xl font-bold text-center text-purple-700 mb-3">Our AI Creates Magic</h3>
            <p className="text-gray-600 text-center">
              Our AI crafts a personalized story with beautiful images and narration.
            </p>
          </div>
          
          <div className="bg-white p-6 rounded-xl shadow-md">
            <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mb-4 mx-auto">
              <span className="text-2xl font-bold text-blue-600">3</span>
            </div>
            <h3 className="text-xl font-bold text-center text-purple-700 mb-3">Enjoy Your Fairytale</h3>
            <p className="text-gray-600 text-center">
              Read, listen to, or download your unique story to enjoy anytime.
            </p>
          </div>
        </div>
      </div>

      <div className="bg-gradient-to-r from-purple-100 to-pink-100 p-8 rounded-2xl shadow-md my-16">
        <div className="text-center">
          <h2 className="text-3xl font-bold text-purple-800 mb-4">Ready to Create Your Magical Story?</h2>
          <p className="text-xl text-gray-700 mb-8">
            Every child deserves a story that speaks to their heart.
          </p>
          <Link 
            to="/create" 
            className="bg-gradient-to-r from-purple-600 to-pink-500 hover:from-purple-700 hover:to-pink-600 text-white font-bold py-3 px-8 rounded-full shadow-lg transform transition-all duration-300 hover:scale-105 inline-block"
          >
            Start Creating Now
          </Link>
        </div>
      </div>
    </div>
  );
};

export default HomePage; 