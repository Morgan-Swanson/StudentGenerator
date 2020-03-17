import ReactDOM from 'react-dom';
import './scholar.css';
import React from "react";
 
class ResumePrev3 extends React.Component
{
    render(){
        return   <div className = "allresu3">
           
            <div class="resu3">
            <h1>BIO</h1>
            <h2>__________</h2>
            <img src='/Bio.png' alt='test'/>
            <h1>ClASS SCHEDULE</h1>
            <h2>__________</h2>
            <div class="image2">
            <img src='/resume.png' alt='test'/>
            </div> 
            <div class="image3">
            <img src='/schedule.png' alt='test'/>
            </div> 
            <h3>RESUME</h3>
            <h4>__________</h4>
            </div>
             
           
        </div> 
        
     
    }

}

class Together2 extends React.Component{
  //Combines my Event class and the DivTest Class.
  render(){
      return <div>
          <ResumePrev3></ResumePrev3>
         
      </div>

  }
}





ReactDOM.render(<Together2 />, document.getElementById('root'));

 
export default Together2;