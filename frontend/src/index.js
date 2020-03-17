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


class YearSlider extends Component {
    constructor(props, context) {
      super(props, context)
      this.state = {
	  volume: 0,
	  options: ["1st", "2nd", "3rd", "4th"]
      }
    }
  
    handleOnChange = (value) => {
      this.setState({
        volume: value
      })
    }
   
  
    render() {
      let { volume } = this.state
      return (
	<div className="slide">
	<h1>Student Year</h1>
	<div className="inslide">
        <Slider
	  tooltip = {true}
          format ={this.display}
          step = {25}
          value={this.options[volume / 25]}
          orientation="horizontal"
          onChange={this.handleOnChange}/>
        </div>
	</div>
      )
    }
}

class GenderSlider extends Component {
    constructor(props, context) {
      super(props, context)
      this.state = {
	  volume: 0,
	  options: ["Male", "Female"]
      }
    }
  
    handleOnChange = (value) => {
      this.setState({
        volume: value
	})
    }
   
  
    render() {
      let { volume } = this.state
      return (
	<div className="slide">
	<h1>Student Gender</h1>
	<div className="inslide">
        <Slider
	  tooltip = {true}
          format ={this.display}
          step = {100}
          value={this.options[volume / 100]}
          orientation="horizontal"
          onChange={this.handleOnChange}/>
        </div>
	</div>
      )
    }
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
    render(){
        return <div className="info"> 
        <div id="rectangle" ></div>
        </div>; 
    }
    
}

function Resume(props) {
    return (
        <div class="resu">
            <h1>{props.name}</h1> 
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



class Together extends React.Component{
    constructor() {
	super()
	    this.state = {student: [{"name": "STUDENT1", "gender": "NONE", "hometown": "NONE", "ethnicity": "NONE"},
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
	fetch("/api/8")
	    .then(data => data.json())
	    .then(data => this.setState({student: data}))
	    }
    render(){
        return <div>
            <DivTest></DivTest>
            <GenderSlider></GenderSlider>
            <YearSlider></YearSlider>
            <Bottomborder></Bottomborder>
            <ResumePrev2 data={this.state.student.slice(0,4)}></ResumePrev2>
       	    <ResumePrev data={this.state.student.slice(4,8)}></ResumePrev>
          
        </div>

    }
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