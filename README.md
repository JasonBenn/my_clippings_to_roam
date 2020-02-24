# My Clippings.txt -> Roam

This little script is meant to parse My Clipping.txt files from Kindle devices and print them to the terminal in a format suitable for copy-pasting into Roam.

![image](https://user-images.githubusercontent.com/2539761/75123278-d93e3700-565a-11ea-8170-f2452f70d570.png)
_From left to right: My Clippings.txt, the output of this script, and the final document in Roam._

## Usage

1. To configure, update the values of MY_CLIPPINGS_PATH and CUSTOM_HASHTAGS.
2. Invoke the script without any arguments to see a sorted list of documents and books with the number of highlights in each:
```
> python parse.py
 31: Digital Minimalism (Cal Newport)
105: Poor Charlie's Almanack - Charlie Munger
 15: Self-Attention Generative Adversarial Networks - Zhang
```
3. To filter results of any individual document or book, pass a query to the command. Any documents with matching titles (case insensitive) will be printed:
```
> python parse.py po
 31: Digital Minimalism (Cal Newport)
105: Poor Charlie's Almanack - Charlie Munger
```
4. And once you've got a query that only matches one document, all of your highlights will be printed to the console in a format suitable for one page in Roam in a [style inspired by Nat Eliason](https://twitter.com/jasoncbenn/status/1227746265724702720). The outputted `Tags::` line will include any date on which you made a highlight for this document (in other words, if I read a book over the course of a week and made highlights on 3 different days, all 3 days will be represented).
```
> python parse.py poor
Poor Charlie's Almanack - Charlie Munger
Tags:: #[[February 20th, 2020]] #[[February 22nd, 2020]] #[[Charlie Munger]] #[[TODO]]
- "It's a sad thing, but not everybody loves me."
- [Franklin] left behind a full record of an old age that was among the most constructive and happy euer lived...
...
```

If you've got any feedback, @ me in the [Roam Research Slack](https://roamresearch.slack.com/join/shared_invite/enQtODg3NjIzODEwNDgwLTdhMjczMGYwN2YyNmMzMDcyZjViZDk0MTA2M2UxOGM5NTMxNDVhNDE1YWVkNTFjMGM4OTE3MTQ3MjEzNzE1MTA) in the #hacking channel or on [Twitter](https://twitter.com/jasoncbenn), or send me an email at jasoncbenn@gmail.com! 

## Other tips

I use [Calibre](https://calibre-ebook.com/)'s experimental "Fetch Annotations" function to get highlights from my Kindle docs.
