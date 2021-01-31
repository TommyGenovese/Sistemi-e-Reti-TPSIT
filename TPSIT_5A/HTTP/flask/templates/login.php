<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="shortcut icon" href="../static/images/logo.png">
    <style type="text/css">
        box-grad{
            background-image: linear-gradient(top bottom, #FFFFFF 0%, #AACFEF 100%);
        }
    </style>
    <title>Login</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
</head>
    
</head>
<body>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
    <div class="riga">
        <div class="col">
            <nav class="navbar navbar-expand-xl navbar-expand-lg navbar-expand-md navbar-light bg-info">
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <a class="navbar-brand" href="#">
                    <img src="../static/images/logo.png" width="60" height="60" class="d-inline-block align-top" alt="" />
                </a>
                <div class="collapse navbar-collapse" id="nav-content">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item active">
                        <a href="../" class="nav-link" style="font-size: 20px;">Home</a>
                    </li>
                    <li class="nav-item">
                        <a href="#fit" class="nav-link" style="font-size: 20px;">Centro Fitness</a>
                    </li>
                    <li class="nav-item">
                        <div class="dropdown">
                            <button class="btn btn-info dropdown-toggle nav-link" type="button" id="cors" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true" style="font-size: 20px;">
                                Corsi
                            </button>
                            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                <a class="dropdown-item" href="#">Aerobica</a>
                                <a class="dropdown-item" href="#">Tone Up</a>
                                <div class="dropdown-divider"></div>
                                <a class="dropdown-item" href="#">Posturale</a>
                                <a class="dropdown-item" href="#">Total Body</a>
                                <a class="dropdown-item" href="#">GAG</a>
                                <div class="dropdown-divider"></div>
                                <a class="dropdown-item" href="#">Zumba</a>
                                <a class="dropdown-item" href="#">Yoga</a>
                            </div>
                        </div>
                    </li>
                    <li class="nav-item">
                        <a href="#pt" class="nav-link" style="font-size: 20px;">Personal Trainer</a>
                    </li>
                    <li class="nav-item">
                        <a href="#" class="nav-link" style="font-size: 20px;">Dove siamo?</a>
                    </li>
                    <li class="nav-item">
                        <a href="login" class="nav-link" style="font-size: 20px;">Login</a>
                    </li>
                </ul>
                <form class="form-inline my-2 my-lg-0">
                    <input class="form-control mr-sm-2 bg-light" type="cerca" placeholder="Cerca" aria-label="Cerca">
                    <button class="btn btn-outline-light  my-2 my-sm-0" type="submit">🔍</button>
                </form>
                </div>
            </nav>
        </div>
    </div>
    <br>
    <div class = "container">
        <div class="input-group-text flex-nowrap">
            <form class="form-inline my-2 my-lg-0" method="POST" action="">
                <input type="text" class="form-control" name="InputUsername" placeholder="Username" aria-label="Username" aria-describedby="addon-wrapping">
                <input type="password" class="form-control" name="InputPassword" placeholder="Password" aria-label="Password" aria-describedby="h">
                <button class="btn btn-outline-primary  my-2 my-sm-0" type="submit">Invio</button>
            </form>
            <form action="logged.php" method="POST">
                <input type="text" name="InputUsername" placeholder="Username" /><br>
                <input type="password" name="InputPassword" placeholder="Password" /><br>
                <input type="submit" value="LogIn"/>
            </form>
        </div>
    </div>
</body>
</html>