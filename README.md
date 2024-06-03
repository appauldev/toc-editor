# Generating Table of Contents with pdf.tocgen
## Prerequisites
1. Install python and create a new project
2. Create and activate a virtual environment for the project
3. Install [pdf.tocgen](https://pypi.org/project/pdf.tocgen/) with `poetry add pdf.tocgen` or `pip install pdf.tocgen`. Note that I am using `poetry` for the following instructions, so kindly change them to the appropriate commands if you are using `pip`

## Workflow
**NOTE:** This basic workflow suits my current needs, and you can always modify it to suit yours! Kindly consult [pdf.tocgen](https://pypi.org/project/pdf.tocgen/) for a more comprehensive documentation of the tool.

### 1. Determining the heading attributes

The headings of the PDF file can be used as the basis to get the table of contents (TOC). Since these headings have different attributes, i.e., different font sizes, names, placement on the page, etc., we need to determine them before we can generate the TOC. To do this, we use the following command:

```bash
poetry run pdfxmeta -a 1 -p 54 in.pdf "Heading 1 text" >> recipe.toml
```
Here's the breakdown of the command:

* `pdfxmeta` is a tool provided `pdf.tocgen` to extract the attributes of the search phrase in the command ("Heading 1 title")
* `-a 1` automatically generates the attribute for `Heading 1`. Make sure to change `1` with the appropriate heading number (i.e., 2 for heading 2, 3 for heading 3 and so on.)
* `-p 54` is where we will search the heading that contains the search phrase.

    * **NOTE:** There could be multiple instances of your search phrase on a page. Hence, try to look for a heading with a unique phrase and use this and its page number for the command

* `in.pdf` is our pdf
* `recipe.toml` is where the attributes of the specified heading will be written, something like:
```toml
[[heading]]
# Introduction
level = 1
greedy = true
font.name = "SomeFontNameBold"
font.size = 25
# other attributes

[[heading]]
# Introduction
level = 2
greedy = true
font.name = "SomeFontNameBoldItalic"
font.size = 18
# other attributes
```
We complete the recipe by ***manually*** inspecting and finding different headers of the PDF. 

Hence, this process can take some time depending on how complex your PDF is, and will depend on how much you want to customize your TOC. You can even add figures and tables in your TOC if they have a regular pattern for each page!

### 2. Extracting the heading attributes
Now that we have the attributes of the header, we can extract it by using the following command
```bash
poetry run pdftocgen in.pdf < recipe.toml > raw_toc.txt
```
* Using the `recipe.toml` we generated previously, we use `pdftocgen` to generate the TOC
* `raw_toc.txt` will contain the generated TOC. It will look something like this:
```
"Cover" 1
"Copyright" 4
"Table of Contents" 5
"Preface" 9
    "Why We Wrote This Book" 9
    "Who This Book Was Written For" 11
    "How This Book Is Organized" 12
    "Acknowledgments" 15
"CHAPTER 1 Introduction" 17
    "An intro" 18
    "Where to start" 19
    "Some tips" 25
```
**NOTE:** The first line `"Cover" 1` is manually added for the cover page. Depending on your PDF, you may need to ***manually*** add some pages to complete your TOC

### Cleaning and transforming the generated TOC
This part can be optional if the generated raw TOC is already enough for your needs. However, since the generated TOC is just a text file, you can always modify it based on your needs.

For example, some extracted headings may have poorly formatted strings (e.g. `Chapter 2Introduction` instead of `Chapter 2: Introduction`). In this case, you can use any tools of your choice to go through each line of the generated TOC to perform the corresponding cleaning and transformations

**NOTE:** The lines of the generated TOC will have tabs for headings 2 to N and each extracted heading will always be enclosed with a `"`, so keep this in mind when modifying the TOC!

### Integrating the TOC to the PDF
To use your generated or modified TOC as the new TOC of your PDF, you can use the following command:
```bash
poetry run pdftocio in.pdf < your_toc.txt -o updated.pdf
```
* We use `pdftocio` to update the TOC of `in.pdf` with `your_toc.txt`
* We specify the output pdf with `-o updated.pdf`

### Verify the updated PDF
Check your PDF if the table of contents is correct! If not, you can always modify the generated TOC, or you can check again the recipe if you got the correct attributes for your headers.

