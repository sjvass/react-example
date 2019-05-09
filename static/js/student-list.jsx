"use strict";
/*Example of getting and using data from server*/

//Defines StudentList tag
class StudentList extends React.Component {
    //getting attributes from superclass' 
    //(React.Component) constructor
    constructor(props) {
        super(props);
        //setting state attribute's inital value 
        //to have studentInfo key with an empty list
        this.state = {studentInfo: []};
    }

    //overriding super's componentDidMount method
    //componentDidMount is a method that executes
    //as soon as loading completes
    componentDidMount() {
        //calls getStudentInfo()
        this.getStudentInfo();
    }

    //Method that makes a get requst to
    //route that returns student info
    getStudentInfo() {
        //request
        fetch('/api/students')
        //specify request results are JSON type
        .then(response => response.json())
        //store results in state attribute so
        //they can be accessed by other methods
        .then(data => {
            //sets the value of studentInfo to the list
            //returned by the route
            this.setState({studentInfo: data})
            //console.log(data)
        })
    }

    render() {
        //console.log(this.state.studentInfo);

        //save state as a variable for easy access
        const students = this.state.studentInfo;

        //use js map function (similar to a list comprehension)
        //for each value in students, create an <li> element
        //with the student's id as a key and a value of their
        //first and last names. If your data is not a list,
        //you don't need this.
        //this could also be done with a for loop
        const nameList = students.map((student) =>
            <li key={student.student_id.toString()}>
                {student.fname} {student.lname}
            </li>
        );

        //returns the list of html formatted <li>s wrapped
        //in the <ul> tag.
        //there can't be any js in the return statement, so
        //all looping, processing, etc. has to be done before
        //the return and formatted as html.
        return(
            <ul>
                {nameList}
            </ul>
        );
    }
}

//Specifies what and where to render html
ReactDOM.render(
    //html tags
    <div id="wrapper">
        <StudentList />
    </div>,
    //render element
    document.getElementById('root')
);