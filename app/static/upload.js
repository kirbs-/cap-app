$(document).ready(() => {
    // add upload button handler
    $('#upload-form-btn').click( evt => {
        // block link from processing
        evt.preventDefault();

        let $upload_form = $('#upload-form');

        // setup form data object to handle async multipart file upload.
        let form_data = new FormData();
        form_data.append('file', $('#file')[0].files[0]);

        // hide upload modal

        let url = $upload_form.attr('action');
        let method = $upload_form.attr('method');

        $.ajax({
            url: $upload_form.attr('action'), // grab url from form
            type: $upload_form.attr('method'), // grap request method from form
            data: form_data,
            processData: false,
            contentType: false,
            success: add_upload_file_row,
            // error: show_error_message,
        })

        $('#upload-modal').modal('hide');
    });
});


// const upload_btn_handler = () => {
//     // Process upload button click via ajax.

//     // add a click event callback
    
// }

const add_upload_file_row = html => {
    // append HTML partial to 'main-table'
    $('#main-table').append(html);
}

// const show_error_message = data => [
//     // display text in error flash

// ]