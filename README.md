mynaa
=====

Python CLI tool to post a lengthy tweet as a series. 

Lot of times you would want the reach of twitter but it's quite restrictive about what you want to express. Get around it with mynaa.

Features
========

  1)Truncates whole words only
  
  2)Tweet pagination
  
  3)Pure cli for absolute security and control
  
  4)Reverse order posting for readability

Installation
============

Please read INSTALL

Usage
=====

./mynaa.py 'Your tweet text'

Note: Everytime you run the above command - you would be presented with the following authentication procedure:

    "Copy and paste the beside url in browser to get pin: http://api.twitter.com/oauth/authorize?oauth_token=XXXXXXXX"
    "Enter acquired PIN to proceed:"

Copy and paste the url in the browser and authorize the app to post. You would be provided with a PIN after authorization. Please enter the PIN at command prompt and press enter to post the tweet. The above mentioned procedure has to be followed evertime you want to post.

Example
=======

./mynaa.py "The quick brown fox jumps over the lazy dog is an English-language pangram – a phrase that contains all of the letters of the alphabet. It has been used to test typewriters and computer keyboards, and in other applications involving all of the letters in the English alphabet. Owing to its brevity and coherence, it has become widely known."
