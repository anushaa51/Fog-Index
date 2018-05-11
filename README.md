
<h1 align = "center"> Fog Index & Gunning Fog Index Calculator</h1> 
<h4 align = "center">Python script to calculate the Gunning Fog Index & Fog Index of a text document.</h4>
<br><hr>
<h2> What is it?</h2>
<h3> Gunning Fog Index</h3>
The Gunning fog index is a readability test commonly used to evaluate how easily some text can be read by its intended audience.
It is calculated as follows : 
<p align = "center">  <strong> Gunning Fog Index = </strong>  <img align = "center" src = "https://wikimedia.org/api/rest_v1/media/math/render/svg/84cd504cf61d43230ef59fbd0ecf201796e5e577" >
</p>
Complex words : Words with 3 syllables or more, that are not compound words.<br>
Compound words : Words that are a combination of 2 or more smaller words. For example, "multinational" is made up of the words "multi" and "national".
<br>
<h3>Fog Index</h3>
<p align = "center"> <strong> Fog Index = </strong> <img align = "center" src = "https://imgur.com/a/2PWx1gn.png"></p>

<h4> Note : </h4>

This project is inclusive of a `syllable counter` function, and a `compound word splitter` function. They can be used independently by changing the interfaces between the functions.

The compound word splitter function was provided by [Gokul VSD](https://github.com/GokulVSD/FOGIndex). It uses the Python module named `PyEnchant`, which is compatible with Linux and only the 32 bit Python on Windows as of May 2018.
<br>
Currently, the project takes its input from a text document and gives its output to another text document. It was made as part of an assignment in Software Engineering, in semester 4 of my engineering course. <br><br>
<h3> Sample Outputs</h3>
Successful output :

`The Fog Index of the given text document is 9.485714285714286`  
`The Gunning Fog Index of the given document is 9.194805194805195`  
`Total number of sentences = 7`  
`Total number of words = 110`  
`Total number of words with 3 or more syllables = 8`
<br><br>
Unsuccessful output :  
`File does not exist, please try again by placing a valid file named 'TestDocument.txt' in current directory`
