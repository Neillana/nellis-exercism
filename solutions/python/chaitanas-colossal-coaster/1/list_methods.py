"""Functions to manage and organize queues at Chaitana's roller coaster."""
import copy


def add_me_to_the_queue(
    express_queue: list[str],
    normal_queue: list[str],
    ticket_type: int,
    person_name: str
    ) -> list[str]:
    """Add a person to the express or normal queue depending on the ticket type.

    Example:
        >>> add_me_to_the_queue(["Tony", "Bruce"], ["RobotGuy", "WW"], 1, "RichieRich")
        ["Tony", "Bruce", "RichieRich"]
    """
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    
    normal_queue.append(person_name)
    return normal_queue


def find_my_friend(queue: list[str], friend_name: str) -> int:
    """Search the queue for a name and return their queue position (index).

    Example:
        >>> find_my_friend(["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], "Steve")
        1
    """
    if friend_name not in queue:
        raise ValueError("Friend is not in queue!")
    return queue.index(friend_name)


def add_me_with_my_friends(queue: list[str], index: int, person_name: str) -> list[str]:
    """Insert the late arrival's name at a specific index of the queue.

    Example:
        >>> add_me_with_my_friends(["Natasha", "Steve", "T'challa"], 1, "Bucky")
        ["Natasha", "Bucky", "Steve", "T'challa"]
    """
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: list[str], person_name: str) -> list[str]:
    """Remove the mean person from the queue by the provided name.

    Example:
        >>> remove_the_mean_person(["Steve", "Eltran", "Wanda"], "Eltran")
        ["Steve", "Wanda"]
    """
    queue.remove(person_name)
    return queue
    

def how_many_namefellows(queue: list[str], person_name: str) -> int:
    """Count how many times the provided name appears in the queue.

    Example:
        >>> how_many_namefellows(["Natasha", "Steve", "Eltran", "Natasha"], "Natasha")
        2
    """
    return queue.count(person_name)


def remove_the_last_person(queue: list[str]) -> str:
    """Remove the person in the last index from the queue and return their name.

    Example:
        >>> remove_the_last_person(["Steve", "Eltran", "Natasha", "Rocket"])
        "Rocket"
    """
    if not queue:
        raise ValueError("Queue is empty!")
    return queue.pop()
    

def sorted_names(queue: list[str]) -> list[str]:
    """Sort the names in the queue in alphabetical order and return the result.

    Example:
        >>> sorted_names(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
        ['Eltran', 'Natasha', 'Natasha', 'Rocket', 'Steve']
    """
    # copied_queue = copy.deepcopy(queue)
    # copied_queue.sort()
    # return copied_queue
    return sorted(copy.deepcopy(queue))