import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; 
import * as serviceWorker from './serviceWorker';
import YearSlider from './Volume';
import 'react-rangeslider/lib/index.css';
import { Component } from 'react'
import Slider from 'react-rangeslider'
import {
  Route,
  NavLink,
  HashRouter
} from "react-router-dom";
import Together2 from "./scholar";


class GenderSlider extends Component {
    constructor(props, context) {
      super(props, context)
      this.state = {
        volume: 0
      }
    }
  
    handleOnChange = (value) => {
      this.setState({
        volume: value
      })
    }
   
  
    render() {
      let { volume } = this.state
      return (<div className="inslide">
        <Slider
          tooltip = {true}
          format ={this.display}
          step = {10}
          value={volume}
          orientation="horizontal"
          onChange={this.handleOnChange}/>
        </div>
      )
    }
  }


  
 
const Slide = () => (
    <div className="slide">
    <h1>STUDENT YEAR</h1>
    
    
      <YearSlider />
    </div>
  );

    
const Slide2 = () => (
<div className="slide2">
<h1>STUDENT PERSONALITY</h1>
    <GenderSlider />
</div>
); 


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
		{props.map(student => 
			   <Resume name={student.name}
			   gender={student.gender}
			   hometown={student.hometown}
			   ethnicity={student.ethnicity}>
                    </Resume>
                    <div className="content">
                    <Route exact path="/scholar" component={Together2}/>
                    </div>
                </div>
            </HashRouter>); 
}


class ResumePrev2 extends React.Component
{

    render(){
        return <HashRouter>
	    <p>My Token = {window.token}</p>
        <div className = "allresu2">
            <div class="resu">
            <h1>SCHOLAR 2</h1> 
            <a href="#link 1">NAME</a>
            <h3>GENDER</h3>
            <h3>HOME TOWN</h3>
            <h3>ETHNICITY</h3>
            <h2>______________________ </h2>
            </div>
            <div class="resu">
            <h1>SCHOLAR 4</h1>  
            <a href="#link 2">NAME</a>
            <h3>GENDER</h3>
            <h3>HOME TOWN</h3>
            <h3>ETHNICITY</h3>
            <h2>______________________ </h2>
            </div>
            <div class="resu">
            <h1>SCHOLAR 6</h1>  
            <a href="#link 3">NAME</a>
            <h3>GENDER</h3>
            <h3>HOME TOWN</h3>
            <h3>ETHNICITY</h3>
            <h2>______________________ </h2>
            </div>
            <div class="resu">
            <h1>SCHOLAR 8</h1>  
            <a href="#link 4">NAME</a>
            <h3>GENDER</h3>
            <h3>HOME TOWN</h3>
            <h3>ETHNICITY</h3>
            </div>
        </div>
      </HashRouter>
     
    }

}




class Together extends React.Component{
    constructor() {
	super()
	this.state = {student: null,
	};    
    }

    componentDidMount() {
	fetch("/api/1")
	    .then(data => data.json())
	    .then(data => this.setState({student: data}))
	    }
    render(){
        return <div>
            <DivTest></DivTest>
            <Slide></Slide>
            <Slide2></Slide2>
            <Bottomborder></Bottomborder>
            <ResumePrev2></ResumePrev2>
            <ResumePrev data={this.student}></ResumePrev>
           
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