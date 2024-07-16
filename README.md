<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile</title>
    <style>
        #para1
        {
            text-align: center;
            margin: auto;
            font-size: 60px;
            margin-bottom: 0px;
            padding: 10px;
            justify-content: center;
        }
        #img1
        {
            height: 300px;
            display: block;
            margin-left: auto;
            margin-right: auto;
            border:10px solid black;
            border-radius: 500px;
            justify-content: center;
        }
        #div1
        {
            margin: auto;
            width: 550px;
            margin-left: 250px;
        }
        .input1
        {
            padding: 5px;
            width: 800px;
            font-size: 25px;
            background-color: red;
            border: 5px solid black;
            
        }
        .label1
        {
            margin-top: 0px;
            font-size: 40px;
            padding: 10px;
        }
        body
        {
            background-color:bisque;
        }
        #update1
        {
            height: 45px;
            width: 200px;
            margin-top: 20px;
            font-size: 30px;
            background-color: red;
            color: white;
            margin-left: 290px;
            border:5px solid black;
            border-radius: 15px;
        }
    </style>
</head>
<body>    
    <p id="para1">Welcome Your Profile</p>
    <img id="img1" src="manicon.jpg" alt="Loading...">
    <div id="div1">
        <form action="something.py">
            <label for="" class="label1">Name:</label>
            <br><input type="text" class="input1" required>
            <br><label for="" class="label1">Contact No:</label>
            <br><input type="number" class="input1" required>
            <br><label for="" class="label1">Email:</label>
            <br><input type="text" class="input1" required>
            <br><label for="" class="label1">Year:</label>
            <br><input type="number" class="input1" required>
            <br><label for="" class="label1">Roll no:</label>
            <br><input type="text" class="input1" required>
            <br><label for="" class="label1">Enrollment No:</label>
            <br><input type="number" class="input1">
            <br><input type="submit" value="Update" id="update1">
        </form>
    </div>
</body>
</html>
