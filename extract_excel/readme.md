# Generate code from AI tool

- install cursor
- create a new main.py file and open it
- press cmd+k to open a dialog for editing instructions. input following commands and hit enter key. It will display a candidate code waiting for confirmation. press cmd+enter if yes.
    ```
    write a python program to extract data from all of the excel files in current folders recursively. the excel files contain multiple sheets, the first line of each sheet is title and the following lines are different detail information. define a data model as the title and store the data in a sqlite db. using python, xlsx library.
    ```
- debug the code with Python run and debugger extention in cursor. if the extention doesn't exist, download it in the plugin extention store.
- type in the following commands when encountering problem. locate on the error line and hit cmd+k and type in
    ```
    there some situation that the number of columns in data is less than the number of definition in table, add some judement here
    ```

    ```
    there are some situation that the first column in data is always 'nan', which is meanless, get rid of this meanless column if the number of bindings supplied greater than definition in table
    ```

    ```
    add judgement here to skip create table when the table already exists
    ```

    ```
    there is a situation that column 2, column 3 are null in data, add some filter judgement here to delete those rows with null
    ```

It seems that the developer only need to debug and give instructions and the AI workds like an efficient assistant. Programmer need to think the reason and optimize the solution and architecture.