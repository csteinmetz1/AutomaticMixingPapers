# audiodata
Community driven index of datasets for audio and music research

## Overview
There are many lists available that document various audio datasets for research in audio and music. Most of these lists are maintained by individuals, and therefore often become out of date and no longer maintained. The goal of this project is to create a similar list of datasets that can easily be maintained by the community so as to remain both comprehensive and up to date.

## Contributing
Adding a new dataset is simple. First fork this repository and clone a local copy. Then create a new entry in the JSON file located at `data/datasets.json`. Include the same keys and data as shown in the example below. 

```
{
	"name" : "Million Song Dataset",
	"description" : "A freely-available collection of audio ...",
	"category" : "music recordings",
	"year" : "2011",
	"size" : 273,
	"length" : "1,000,000 tracks",
	"audio" : "Yes",
	"homepage" : "http://millionsongdataset.com/",
	"download" : "https://aws.amazon.com/datasets/million-song-dataset/"
}
```

To preview the site on your local machine you must serve the page locally and view it in your browser. 

You can do this with Python (my preferred way),
```
python3 -m http.server
```

with Node.js,
```
npm install http-server -g
http-server -p 8000
```
or any other way your prefer.

Finally make a pull request on this repository with your changes.

## Reference lists
These lists were used partly in the creation of this list and should be credited.