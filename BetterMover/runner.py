import logging

from .SmartMover import SmartMover

LOG_LVL = logging.WARN

def setup_logger():
	logging.basicConfig(level=LOG_LVL)
	return logging.getLogger(__name__)

def main():
    _ = setup_logger()

    mover = SmartMover()
    dir = "\\\\DAEDALUS2\\Media\\Movies"
    mover.smart_move_directory(dir)

if __name__ == "__main__":
	main()



########################################################################
#                               Requirements
########################################################################

# GIVEN a directory with many potential files,
# FIRST determine all potential files
# THEN assert they are valid files
#   Valid: non-empty, exists, typed
# AND clean the validated files,
#   Clean: conforms to the format "I am a FileName - With Potential Details.xyz"
# THEN move the cleaned files to new parents
