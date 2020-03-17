import React, { Component } from 'react'
import Slider from 'react-rangeslider'

class TestSlider extends Component {
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
        onChange={this.handleOnChange}
      />
      </div>
    )
  }
}


export default TestSlider 
