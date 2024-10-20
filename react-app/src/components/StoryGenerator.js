// StoryGenerator.js
import React, { useState } from 'react';
import axios from 'axios';
import './StoryGenerator.css';

function StoryGenerator() {
	const [story, setStory] = useState('');
	const [vocabList, setVocabList] = useState(['word1', 'word2']); // Example vocab list
	const [loading, setLoading] = useState(false);

	const generateStory = async () => {
    	setLoading(true); // Set loading state to true
    	try {
        	const response = await axios.post('http://localhost:3000/generate_story', {  // Update with your Flask server's IP
            	vocab_list: vocabList,
            	language: 'English',
            	topic: 'daily life',
            	level: 'intermediate',
            	length: 100,
        	});
        	setStory(response.data.story);
    	} catch (error) {
        	console.error('Error generating story:', error);
        	setStory('Error generating story, please try again.'); // Set error message
    	} finally {
        	setLoading(false); // Reset loading state
    	}
	};

	return (
    	<div>
        	<button className= "generate-story" onClick={generateStory} disabled={loading}>
            	{loading ? 'Generating...' : 'Generate Story'}
        	</button>
        	{story && <p>{story}</p>}
    	</div>
	);
}

export default StoryGenerator;
