Python Command Line Interface tool to manage To-Do tasks. Designed to re-learn the basics of python before beginning to understand more advanced topics using it as a tool.

| Command | Option Location | Implemented or Not | Option's Intended Purpose                                                                                                                   |
| :-----: | :-------------: | :----------------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| View    | Main Menu       | Implemented        | Menu Navigation and task viewing. Go from the Main Menu to the View Menu. The Read (R) of CRUD.                                             |
| Exit    | Main Menu       | Implemented        | Menu Navigation. Exiting the program in a way that saves to file before exiting to maintain tasks throughout program runs.                  |
| Return  | View Menu       | Implemented        | Menu Navigation. Go back from View Menu to Main Menu.                                                                                       |
| Add     | View Menu       | Implemented (Buggy)| Add a new task to list / Make new task. The Create (C) of CRUD.                                                                             |
| Update  | View Menu       | Not Implemented    | Update a currently existing task. Verify correct task is updated and deal with collisions easily. The Update (U) of CRUD.                   |
| Delete  | View Menu       | Not Implemented    | Delete a currently existing task. Verify the right task is what gets deleted and handle collisions without issue. The Delete (D) of CRUD.   |

<p align="center">
  <img src="https://github.com/user-attachments/assets/388e3c9c-15d0-40b6-be07-6e528c78cda3" />
</p>

No notable additional libraries to be installed. Just datetime was used, everything else was coded by hand.

To navigate through menus, simply use the commands typed exactly as written in the table. 

MVP Simply has all commands working and no major bugs with concurrently.

MIT License.
