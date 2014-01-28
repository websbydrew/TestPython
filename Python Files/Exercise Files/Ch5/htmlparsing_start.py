# 
# Example file for parsing and processing HTML
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)


def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()

  # open the sample HTML file and read it
  f = open("samplehtml.html")
  if f.mode == "r":
    contents = f.read() # read the entire file
    parser.feed(contents)
    

if __name__ == "__main__":
  main();
  