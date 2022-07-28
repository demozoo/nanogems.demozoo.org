# Nanogem nanoblog-system

Nanogems website. 

With nanopage, a custom content manager script in python 3.

## Add a new entry

* Clone locally your `git clone `
* Get a virtual env `python -m venv env` and start it 
  * Linux / MacOs `. env/bin/activate`
  * Windows `env\Script\activate`
* Install dependncies `pip install -r req.txt`
* New entries:
  * From demozoo, get the demozoo id and run `python nanopage add_entry $category $flavor $demozoo_id`
  * From scratch, just create one .json file inside`/public/data/$category/$flavor/your_new_entry.json`
* Check your change 
  * Generate the new html `python nanopage generate`
  * Pre visualize it `cd public; python -m http.server ` and go to http://localhost:8000/
* When happy with change 
    ```
    git add .
    git commit -m "A very informative message"
    git push origin main
    ``` 
If the folk that manage the automation done a good job, the online website will be updated automatically within a minute.