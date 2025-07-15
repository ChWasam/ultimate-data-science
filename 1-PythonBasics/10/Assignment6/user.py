# user.login(username,password)
# user.post(post)
# user.see_all_posts()
# user.signup(username,password)

class User:

    def signup(self, id, username,password):
        with open("./database.txt", "a+") as f:
            entry = f"{id}" + "," + username + "," + password + "\n"
            f.write(entry)
        return "User successfully signed up"

    def login(self, username, password):
        with open("./database.txt", "r+") as f:
            all_entries = f.readlines()
            for entry in all_entries:
                single_entry = entry.split(",")
                single_entry[2] = single_entry[2].rstrip()
                if single_entry[1] == username and single_entry[2] == password:
                    return int(single_entry[0])
        return False


    def post(self, post , user_id):
        with open("./database_post.txt", "r+") as f:
            present = False
            new_list = []
            all_entries = f.readlines()
            for entry in all_entries:
                single_entry = entry.split(",")
                print(int(single_entry[0]))
                print(user_id)
                if user_id == int(single_entry[0]) :
                    present = True
                    single_entry.insert(1,post)
                    new_list.append(",".join(single_entry))
                else:
                    new_list.append(entry)
        if present == False:
            with open("./database_post.txt", "w+") as f:
                entry = f"{user_id}" + "," + post + "\n"
                new_list.append(entry)
                f.writelines(new_list)
        else:
             with open("./database_post.txt", "w+") as f:
                f.writelines(new_list)
        return "Content successfully posted"


    def see_all_posts(self,user_id):
        with open("./database_post.txt", "r+") as f:
            all_entries = f.readlines()
            if len(all_entries) > 0:
                for entry in all_entries:
                    single_entry = entry.split(",")
                    if user_id == int(single_entry[0]):
                        return entry
                return " User Hasn't posted anything  yet "
            else:
                return " User Hasn't posted anything yet "
