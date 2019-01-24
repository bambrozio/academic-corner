import React from "react";

const Intro = (props) => {
    return (
        <header className="Intro-header"> 
        <h2>Welcome {props.user.name}!</h2>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        </header>
    )
}

export default Intro