import os
import pathlib

class CustomerController():
    """ Controller object to perform actions on customer information"""

    def save_photo(self, photo_file):
        """ Storage customer photo file on server and returns a photo url.
        
        Parameters
        ----------
        photo_file: file
            File containing customer photo.
            
        Returns
        -------
        str:
            Stored file path.
        """
        try:
            # Create photos folder in case it does not exist.
            base_path = 'photos'
            pathlib.Path(base_path).mkdir(exist_ok=True)

            # Check if filename already exists adding a numbered suffix in that case.
            filename = photo_file.filename
            counter = 1
            fname, extension = os.path.splitext(photo_file.filename)
            while os.path.isfile(os.path.join(base_path, filename)):
                filename = fname + "(" + str(counter) + ")" + extension
                counter += 1

            file_path = os.path.join(base_path, filename)
            photo_file.save(file_path)

            return file_path

        except Exception as e:
            raise e
