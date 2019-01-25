import React from 'react';

class Form extends React.Component {
    handleChange(event) {
        this.props.handleChange(event);
    }
    handlesSubmit(event) {
        this.props.handlesSubmit(event);
    }
    render() {
        return(
            <form onSubmit={this.props.handlesSubmit}>
                <label>Title:
                    <input 
                    name="currentTitle" 
                    type="text"
                    value={this.props.currentTitle}
                    onChange={this.props.handleChange} />
                </label>
                <textarea 
                name="currentDetails" 
                value={this.props.currentDetails}
                onChange={this.props.handleChange} 
                />
                <div><input type="submit" value="Add note"/></div>
            </form>
        );
    }
}

export default Form;