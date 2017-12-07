import React, { Component } from 'react';

export default class Tester extends Component {

    constructor(props)
    {
        super(props);
        this.state = {userInput: ""};
    }

    handleTextChanged(event) {
        this.setState({userInput: event.target.value});
    }

// {e => this.handleTextChanged(e)} binds "this" by creating a lamda.

    render() {
        return (
            <div>
                <h3>Letters written: {this.state.userInput.length}</h3>
                <h2>{this.props.sentence.split("").map((value, index) => {
                    if(index > this.state.userInput.length - 1) {
                        return <span>{value}</span>;
                    }
                    if(this.state.userInput[index] === value) {
                        return <span style={{ backgroundColor: 'green'}}>{value}</span>
                    }
                    return <span style={{ backgroundColor: 'red'}}>{value}</span>
                })}</h2>
                <textarea onChange={e => this.handleTextChanged(e)}
                    style={{fontFamily: 'Helvetica', fontWeight: 'bold', fontSize: '1.5em',
                    width: this.props.sentence.length * 15, height: '150px', resize: 'none'}}
                />
            </div>
        )
    }
}