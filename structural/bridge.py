# Implementor Interface
class DeviceImplementor:
    def play(self):
        ...


# ConcreteImplementor 1
class Speaker(DeviceImplementor):
    def play(self):
        return "Playing on Speaker"


# ConcreteImplementor 2
class Headphone(DeviceImplementor):
    def play(self):
        return "Playing on Headphone"



class MusicPlayer:
    def __init__(self, device):
        self.device = device

    def play_music(self):
        pass


# RefinedAbstraction 1
class PhonePlayer(MusicPlayer):
    def play_music(self):
        return f"Playing music on Phone: {self.device.play()}"


# RefinedAbstraction 2
class ComputerPlayer(MusicPlayer):
    def play_music(self):
        return f"Playing music on Computer: {self.device.play()}"


speaker_on_phone = PhonePlayer(Speaker())
headphone_on_computer = ComputerPlayer(Headphone())

print(speaker_on_phone.play_music())  # Output: Playing music on Phone: Playing on Speaker
print(headphone_on_computer.play_music())  # Output: Playing music on Computer: Playing on Headphone
