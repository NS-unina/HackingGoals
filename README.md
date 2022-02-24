# Hacking Goals Knowledge Base
Hacking Goal Knowledge Base. The project aims to model the web attacker behavior through a Knowledge Graph. 


### Set up with Docker
Setting up the project is very simple with Docker Container. So, I suggest using the following commands to try this project.

```bash
git clone https://github.com/NS-unina/HackingGoals.git
cd HackingGoals
docker-compose up -d
docker exec hackinggoals_typedb_1 bash -c '/opt/typedb-all-linux/typedb console --script="/tql/script"'
```

## Vaticle-TypeDB: Quick Guide   
### Transaction write data    
If you want to try our schema in your instance of typeDB, you can use this code snippet on TypeDB condole.

```
database create hacking_goal
transaction hacking_goal schema write
    source /tql/hackingGoal.tql
    commit
transaction hacking_goal data write
    source /tql/mydata.tql
    commit
```   

### Match clause   
https://docs.vaticle.com/docs/query/match-clause
### Python API Documentation  
https://docs.vaticle.com/docs/client-api/python 

### Find variables in Vaticle
https://docs.vaticle.com/docs/query/get-query


### Built With

* [Vaticle TypeDB](https://docs.vaticle.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites


### Installation

<!-- USAGE EXAMPLES -->
## Usage


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [] Feature 1
- [] Feature 2
- [] Feature 3
    - [] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Francesco Caturano - francesco.caturano@unina.it
Emanuele De Martino - eman.demartino@studenti.unina.it
Gaetano Perrone - gaetano.perrone@unina.it

Project Link: [https://github.com/NS-unina/HackingGoals](https://github.com/NS-unina/HackingGoals)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>