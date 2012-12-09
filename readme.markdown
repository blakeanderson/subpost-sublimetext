Sublime Text 2 Subpost
=========================

Overview
--------
Post markdown to Subpost.

Installation
------------

Go to your Sublime Text 2 `Packages` directory

 - OS X: `~/Library/Application Support/Sublime Text 2/Packages/`
 - Windows: `%APPDATA%/Sublime Text 2/Packages/`
 - Linux: `~/.Sublime Text 2/Packages/`

and clone the repository using the command below:

``` shell
git clone https://github.com/blakeanderson/sublimetext-subpost.git sublimetext-subpost
```

Settings
--------
For the plugin to work, you will need to update Subpost.sublime-settings

Add your Subpost user id, api token, and hostname, then your set.

`subpost.sublime-settings`

	{
		// Subpost User ID
		"userId": "",

		// Subpost Api Token
		"apiToken": "",

		// Subpost Hostname
		"hostname": ""
	}


Usage
-----

- Open a new file within Sublime Text
- Title your post by using YAML Front Matter

<pre>
	---
	title: This post was created in Sublime Text
	---
	// Followed by the body of the post
</pre>
	
- Open up the Command Palette: `Command-Shift-P`
- Select either: `Subpost: send current file to subpost as a draft` or `Subpost: publish current file to subpost`


Notes
-----
The python yaml module is needed to use this plugin.  You can download it [here](http://pyyaml.org/wiki/PyYAML 

