# 1 - 

# The problem that I was trying to solve was being able to explore a given data set in a clean and easy way. The audience for this could be anyone needing to know specific information about Broadway shows for their own research, whether they are an average person, or a professional in a given field needing to conduct research on this topic. My solution was coming up with a flask app that allowed for me to build a running web that presents a dropdown bar of all of the Broadway shows represented in the data set. The idea was that you could then select the show you wanted to see information for, but it would be represented in a neat table that was easy to understand, even for someone who doesn't usually know how to read certain data formats. 

# 

# 2 - 

# The main module concept or tool that I used was Flask Web Applications.  

# 

# !\[visualization](assets/Screenshot%202025-12-01%20152303.png)

# 

# The data that I am using is data/broadway.csv. It is a csv file that shows information on various aspects of Broadway shows, such as the name, date of each show, theater it took place in, and statistics on features such as attendance and performances. I found the dataset on CORGIS, which allows you to download the csv for free.

# 

# 3 - 

# docker build -t myapp:latest .

# docker run --rm -p 5000:5000 --env-file .env myapp:latest

# curl http://127.0.0.1:5000/health

# 

# 4 - 

# I considered using bash scripting like we did in case 3, and I did take some inspiration from it, but it seemed like there was a better and cleaner way to format and search through the data for information. I also wanted it to be more easily accessible for other users. I also considered using an API, but it seemed like it would be overly complex for the task that I wanted to perform on a singular data set. Some of the tradeoffs for doing this are that Flask Apps can only handle smaller tasks, compared to APIs, which can handle bigger tasks with more requests. Flask Apps run well when there is a simple format and they only need to run requests one at a time without many waiting for that one request to run. For this same reason, they can only easily manipulate and store information for smaller csvs and datasets compared to others that might take up more memory. For secrets, in this project, there are no real secrets and everything uses enviornment variables rather than code that is harder. It uses no personal information, so it has high security and privacy. This project was made to be simple and reproducible. It has certain checks so that we can get validation on if everything is running smoothly. One example of this is the /health check to ensure that it is running and we then use Docker so that others can also use the Flask App. The simplicity of it can be a limitation given it is meant to handle small datasets. 

# 

# 5 - 

# When it comes to the performance of the Flask Web App, it is fairly simple. All that you need to do it click the drop down menu where it says "Select a Broadway Show", select the show that you want to explore, and then click the "Search" button. Once you do this, you can explore the data in the table, which shows all information for each showing of the specified Broadway show. The dataset itself is very small, so it doesn;t take that much memory or space on your given device and it runs efficiently. Through my building of this App, I have been able to verify that everything loads correctly into it and that the /health check returns the correct safety message, showing that it is running properly. 

# 

# 6 - 

# If I were to build onto this or add onto the idea, I would maybe look into configuring an API to allow someone to upload their own dataset and explore their own in the same way. I could also add other forms of exploration, such as graphs through coding packages, like Matplotlib. 

# 

# 7 - 

# GitHub Repo: 

