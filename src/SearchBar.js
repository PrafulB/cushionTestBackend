/* Component to render the text field for the search URL input.
*/

import React from 'react';
import { FormGroup, ControlLabel, FormControl, Button } from 'react-bootstrap';

class SearchBar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      url: ''
    };
  }

  render() {
    return (
      <FormGroup controlId="urlSearchBar">
        <ControlLabel>URL: </ControlLabel>{' '}
        <FormControl 
        type="text" 
        placeholder="https://www.google.com"
        inputRef={input => this.textInput = input} 
        />
        <Button onClick={() => this.props.handler(this.textInput.value)} type="submit">Srape!</Button>
      </FormGroup>
    );
  }
}

export default SearchBar;