# Strings [Miscellaneous]

## Prompt
What is a string?

[greycat.jpg](./files/greycat.jpg)

![Image of prompt](./screenshots/strings-prompt.png)

## Description
Reading the prompt, we suspect that there is a string fed into the image either as text or as part of the image (due to the discolouration at the bottom).

![Cat image](./files/greycat.jpg)

Hence, we try and load the image with an [online tool](https://29a.ch/photo-forensics/#forensic-magnifier) in order to see what can be extracted from the image.

![Analysis page](./screenshots/strings-analysis.png)

After exploring with some of the tools present, the flag was found when inspecting the `String Extraction` tab and a simple `CTRL/CMD-F` to search with the keyword `greyhats`.

![String Extraction](./screenshots/strings-extractor.png)

And we have our flag!

![String Extraction](./screenshots/strings-flag.png)

## Flag
`greyhats{W4y2_T0_H1De_1nf0rm4t10N}`