"use strict";
/*Example of posting to server*/


//Defines NewStudendForm tag
class NewStudentForm extends React.Component {
    //override superclass's constructor
    constructor() {
        super();
        //initalize state with no keys
        this.state = {};
        //bind event handler methods to the this instance
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleFnameChange = this.handleFnameChange.bind(this);
        this.handleLnameChange = this.handleLnameChange.bind(this);

    }

    /*event handler methods (specify behavior
        when an event is triggered)*/

    //when value of fname input changes
    handleFnameChange(event) {
        //creates a state, fname with the value
        //entered into fname input
        this.setState({fname: event.target.value});
    }

    //when value of lname input changes
    handleLnameChange(event) {
        this.setState({lname: event.target.value});
    }

    //when a form is submited
    handleSubmit(event) {
        //prevents from posting with Flask request
        event.preventDefault();
        
        //POST request
        //posts data to new-student post route
        fetch('/new-student', {
            //specifies POST request
            method: 'POST',
            //data to be posted to server
            body: 
                //comverts JSON object into Python readable string
                JSON.stringify(
                    //creates JSON object with 
                    //information to be posted
                    {fname: this.state.fname,
                    lname: this.state.lname}
                ),
            //specifies what datatypes are in request
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        });
    }


    render() {
        /*
            html for new student form
            the on{Event} properties specify what method to call
            when that event is triggered
        */
        return(
            <form onSubmit={this.handleSubmit} method="POST">
                <label>
                    First name:
                </label>
                <input type="text" name="fname" onChange={this.handleFnameChange}/>
                <br/>

                <label>
                    Last name:
                </label>
                <input type="text" name="lname" onChange={this.handleLnameChange}/>
                <br/>

                <button type="submit">Add Student</button>
            </form>

        )
    }
}


//Specifies what and where to render html
ReactDOM.render(
    //html tags
    <div id="wrapper">
        <h2>New Student</h2>
        <NewStudentForm />
    </div>,
    //render element
    document.getElementById("root")
);