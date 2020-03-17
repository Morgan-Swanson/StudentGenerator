import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; 
import * as serviceWorker from './serviceWorker';
import 'react-rangeslider/lib/index.css';
import { Component } from 'react'
import Slider from 'react-rangeslider'
import {
  Route,
  NavLink,
  HashRouter
} from "react-router-dom";
import Together2 from "./scholar";


function GenderSlidey(props) {
    return (
	<div className="slide">
	<h1>Student Year</h1>
	<div className="inslide">
        <Slider
	  min = {0}
    	  max = {4}
          tooltip = {false}
          labels = {{0: "Random", 1: "First", 2: "Second", 3: "Third", 4: "Fourth"}}
	  step = {1}
          value={props.value}
          orientation="horizontal"
          onChange={props.handler}/>
        </div>
	</div>
      )
}

function YearSlidey(props) {
      return (
	<div className="slide">
	<h1>Student Gender</h1>
	<div className="inslide">
        <Slider
	  min = {0}
	  max = {2}
	  tooltip = {false}
	  labels = {{0: "Random", 1: "Male", 2:"Female"}}
          step = {1}
          value={props.value}
          orientation="horizontal"
          onChange={props.handler}/>
        </div>
	</div>
      )
}

class DivTest extends React.Component{
    render() {
        return <HashRouter>
         <div class="menu"> 
            <h1> DIGITAL SCHOLAR </h1>
            <li><NavLink to="/index">REMOVE SCHOLAR</NavLink></li>
        </div>; 
        </HashRouter>
    }
}


class Bottomborder extends React.Component{
    render() {
        return <div className="info"> 
        <div id="rectangle" ></div>
        </div>; 
    }
}

function Resume(props) {
    return (
        <div class="resu">
            <h1>{props.name}</h1> 
	    <h3>{props.year}</h3>
            <h3>{props.gender}</h3>
            <h3>{props.hometown}</h3>
            <h3>{props.ethnicity}</h3>
            <NavLink to="/scholar">
                See Details
            </NavLink>
            <h2>______________________ </h2>
        </div>
    ); 
}

function ResumePrev(props) {
    return (
	    <HashRouter>
	    <div className = "allresu">
		{props.data.map(student => 
			   <Resume name={student["name"]}
				year={student["year"]}
			   gender={student["gender"]}
			   hometown={student["hometown"]}
			   ethnicity={student["ethnicity"]}>
			   </Resume>
			   )}
                    <div className="content">
                    <Route exact path="/scholar" component={Together2}/>
                    </div>
		 </div>
            </HashRouter>); 
}

function ResumePrev2(props) {
    return (
	    <HashRouter>
	    <div className = "allresu2">
		{props.data.map(student => 
			   <Resume name={student["name"]}
				year={student["year"]}
			   gender={student["gender"]}
			   hometown={student["hometown"]}
			   ethnicity={student["ethnicity"]}>
			   </Resume>
			   )}
                    <div className="content">
                    <Route exact path="/scholar" component={Together2}/>
                    </div>
		 </div>
            </HashRouter>); 
}

class BigSlidey extends Component {

    constructor(props, context) {
	super(props, context);
	this.handleOnGender = this.handleOnGender.bind(this);
	this.handleOnYear = this.handleOnYear.bind(this);
	this.refreshData = this.refreshData.bind(this);
	this.state = {
	  gender: 0,
	  year: 0,
	  student : [{"name": "STUDENT1", "gender": "NONE", "hometown": "NONE", "ethnicity": "NONE"},
      {"name": "STUDENT3", "gender": "NONE", "hometown": "NONE", "ethnicity": "NONE"},
      {"name": "STUDENT5", "gender": "NONE", "hometown": "NONE", "ethnicity": "NONE"},
      {"name": "STUDENT7", "gender": "NONE", "hometown": "NONE", "ethnicity": "NONE"},
      {"name": "STUDENT1", "gender": "NONE", "hometown": "NONE", "ethnicity": "NONE"},
      {"name": "STUDENT3", "gender": "NONE", "hometown": "NONE", "ethnicity": "NONE"},
      {"name": "STUDENT5", "gender": "NONE", "hometown": "NONE", "ethnicity": "NONE"},
      {"name": "STUDENT7", "gender": "NONE", "hometown": "NONE", "ethnicity": "NONE"}]
      };
    }

    componentDidMount() {
	this.refreshData()
    }
    
    refreshData() {
	fetch("/api/8-" + parseInt(this.state.gender, 10) + "-" + parseInt(this.state.year, 10))
	.then(data => data.json())
	.then(data => this.setState({student: data}));
    }

    handleOnGender(value) {
	this.setState({gender: value});
    }

    handleOnYear(value) {
	this.setState({year: value});
    }
	
    render() {
	return (
		<div>
		<GenderSlidey value={this.state.gender} handler={this.handleOnGender}/>
		<YearSlidey value={this.state.year} handler={this.handleOnYear}/>
		<button onClick={this.refreshData}> Update </button>
		<ResumePrev2 data={this.state.student.slice(0,4)}/>
		<ResumePrev data={this.state.student.slice(4,8)}/>
		</div>
        );
    }
}

function Together() {
    return (
	    <div>
	    <DivTest/>
	    <Bottomborder/>
	    <BigSlidey/>
	    </div>);
}
ReactDOM.render(<Together />, document.getElementById('root'));

/*
var element = React.createElement('h1', {className:'greeting'}, 'Hello word!');
ReactDOM.render(element, document.getElementById('root'));
*/

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();