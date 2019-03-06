# dash-elasticsearch

An example of integrating Elastic search with Plotly Dash

## Getting Started

1. Download and install Elasticsearch
2. Download this repo
3. Start Elasticsearch
4. Run scrape.py
4. Run elasticUI_dash.py

Then we can then search the collected data and display the search results


### Prerequisites

What things you need to install the software and how to install them

```
Elasticsearch
Plotly Dash
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Install Elasticsearch
Install plotly Dash
```


End with an example of getting some data out of the system or using it for a little demo

## Running the tests

To get things running start the elastic instance
On windows this is done by moving to the "bin" directory and run the "bat" file, eg.
C:\Elastic\elasticsearch-6.5.0\bin>elasticsearch.bat

Then we create and indexand load it with data by running scrape.py eg
python scrape.py

Then we start the Dash App by running the app file eg
python elasticUI_dash.py

![Alt text](demo.png?raw=true "Optional Title")
## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Ross Ashman** - *Initial work* 

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

