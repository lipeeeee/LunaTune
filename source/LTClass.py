import logging
local_logger = logging.getLogger(__name__)

class LTClass:
    """Base class for all `luna-tune` related classes.
        Handles standardized logging & other generic stuff
    """

    def __new__(cls, *args, **kwargs):
        cls.logger = logging.getLogger(cls.__name__)
        local_logger.info("Instantiating class %s", cls.__name__)

        instance = super(LDAClass, cls).__new__(cls)
        return instance

