# Python Email Body Parser
This project is a simple Python script that parses an input text file (`emailbody2.txt`) and extracts structured information such as file paths, test identifiers, dates, and job codes. The results are saved into `result.txt`.

1. **File Paths**  
   - Searches for lines containing `K:\BatchLoadFile`.  
   - Extracts filenames matching the pattern `Batch_ND_*`.  
   - Ensures they have a `.txt` extension.  
   - Outputs full paths like:  
     ```
     K:\BatchLoadFile\Batch_ND_12345.txt
     ```

2. **Test Identifiers**  
   - Captures strings starting with `TEST` followed by additional characters (e.g., `TEST123`).  
   - Example output:  
     ```
     TEST123
     ```

3. **Dates**  
   - Extracts dates in the format **MM/DD/YYYY**.  
   - Example output:  
     ```
     08/15/2025
     ```

4. **Job Codes**  
   - Finds and extracts occurrences of `"BYD"` followed by text.  
   - Example output:  
     ```
     BYD001
     ```

5. **Results File**  
   - Writes all extracted data into `result.txt`.  
   - The file contains one entry per line.


## Regular Expression Tips
These are a compilation of some of the important RegEx concepts I used for this project.

```
import re

# search(pattern, string): return a Match object. Match object has:  span(), string, group(), groups()
#      01234567890123456
txt = "The rain in Spain"      
x = re.search(r"\sS\w+", txt)  # return a Match object
print(x.start())               # => 11
print(x.end())                 # => 17 (end at 17, but not include 17)
print(x.span())                # => (11, 17) (starting index, ending index) 

print(x.string)                # => The rain in Spain  (return the original string passed to search)
print(x.group())               # => " Spain" (there is a space before Spain. It is the pattern \sS\w+: \s-space, then S, then \w+: any word letter)

# group(?): match the parenthesis() string 
txt = "The price of PINEAPPLE ice cream is 20"
x = re.search(r"(\b[A-Z]+\b).+(\b\d+)", txt)       
print(x.group())   # PINEAPPLE ice cream is 20   ( the string matches the pattern)
print(x.groups())  # ('PINEAPPLE', '20')         ( tuple with (\b[A-Z]+\b) and (\b\d+) )
print(x.group(1))  # PINEAPPLE                   (1st parenthesis string match: (\b[A-Z]+\b) )
print(x.group(2))  # 20                          (2nd parenthesis string match: (\b\d+) )

# findall(pattern, string)
txt = "The rain in Spain"
x = re.findall("ai", txt)      # return a list of all occurance
print(x)                       # => ['ai', 'ai']
```
