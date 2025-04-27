import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getStory, downloadPdf } from '../services/api';

const StoryViewPage = () => {
  const { id } = useParams();
  const [story, setStory] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [currentPage, setCurrentPage] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [audioRef, setAudioRef] = useState(null);

  useEffect(() => {
    const fetchStory = async () => {
      try {
        const data = await getStory(id);
        setStory(data);
      } catch (err) {
        setError('Failed to load the story. Please try again later.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchStory();
  }, [id]);

  const handleDownloadPdf = async () => {
    try {
      await downloadPdf(id);
    } catch (err) {
      console.error('Failed to download PDF:', err);
    }
  };

  const toggleAudio = () => {
    if (audioRef) {
      if (isPlaying) {
        audioRef.pause();
      } else {
        audioRef.play();
      }
      setIsPlaying(!isPlaying);
    }
  };

  const nextPage = () => {
    if (story && currentPage < story.pages.length - 1) {
      setCurrentPage(currentPage + 1);
    }
  };

  const prevPage = () => {
    if (currentPage > 0) {
      setCurrentPage(currentPage - 1);
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-bounce text-purple-600 text-4xl">
          ✨ Loading your magical story... ✨
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 rounded">
        <p>{error}</p>
      </div>
    );
  }

  if (!story) return null;

  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-white rounded-3xl shadow-xl overflow-hidden">
        <div className="p-6 md:p-10">
          <h1 className="text-3xl md:text-4xl font-bold text-center text-purple-700 mb-6">
            {story.title}
          </h1>
          
          <div className="flex flex-col md:flex-row gap-8 mb-8">
            <div className="w-full md:w-1/2">
              <div className="relative pb-[56.25%] h-0 rounded-2xl overflow-hidden shadow-lg">
                {story.pages && story.pages[currentPage] && (
                  <img 
                    src={story.pages[currentPage].imageUrl} 
                    alt={`Story page ${currentPage + 1}`}
                    className="absolute top-0 left-0 w-full h-full object-cover"
                  />
                )}
              </div>
              
              <div className="flex justify-between items-center mt-4">
                <button 
                  onClick={prevPage} 
                  disabled={currentPage === 0}
                  className="bg-purple-500 hover:bg-purple-600 text-white font-bold py-2 px-4 rounded-full disabled:opacity-50"
                >
                  ← Previous
                </button>
                <span className="text-gray-600">
                  Page {currentPage + 1} of {story.pages.length}
                </span>
                <button 
                  onClick={nextPage} 
                  disabled={currentPage === story.pages.length - 1}
                  className="bg-purple-500 hover:bg-purple-600 text-white font-bold py-2 px-4 rounded-full disabled:opacity-50"
                >
                  Next →
                </button>
              </div>
            </div>
            
            <div className="w-full md:w-1/2">
              <div className="bg-purple-50 p-6 rounded-2xl shadow-inner h-64 overflow-y-auto">
                {story.pages && story.pages[currentPage] && (
                  <p className="text-lg text-gray-800 leading-relaxed">
                    {story.pages[currentPage].text}
                  </p>
                )}
              </div>
              
              <div className="mt-6">
                <div className="bg-gray-100 p-4 rounded-xl">
                  <div className="flex items-center justify-between mb-2">
                    <button 
                      onClick={toggleAudio}
                      className="bg-pink-500 hover:bg-pink-600 text-white font-bold py-2 px-4 rounded-full flex items-center"
                    >
                      {isPlaying ? (
                        <>
                          <svg className="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zM7 8a1 1 0 012 0v4a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v4a1 1 0 102 0V8a1 1 0 00-1-1z" clipRule="evenodd"></path>
                          </svg>
                          Pause
                        </>
                      ) : (
                        <>
                          <svg className="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clipRule="evenodd"></path>
                          </svg>
                          Listen
                        </>
                      )}
                    </button>
                    
                    <button 
                      onClick={handleDownloadPdf}
                      className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-full flex items-center"
                    >
                      <svg className="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                        <path fillRule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clipRule="evenodd"></path>
                      </svg>
                      Download PDF
                    </button>
                  </div>
                  
                  <audio 
                    ref={ref => setAudioRef(ref)}
                    src={story.audioUrl} 
                    onEnded={() => setIsPlaying(false)}
                    className="w-full"
                    controls
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default StoryViewPage; 