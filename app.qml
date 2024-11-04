import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 600
    height: 100

    title: "HelloApp"

    flags: Qt.FramelessWindowHint | Qt.Window

    property string currTime: "00:00:00"
    property QtObject backend

    Rectangle {
        anchors.fill: parent

        Image {
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: "./images/playas.jpg"
            fillMode: Image.PreserveAspectFit
        }

        Text {
            text: currTime
            font.pixelSize: 48
            color: "white"
        }

    }


    Connections {
        target: backend

        function onUpdated(msg) {
            currTime = msg;
        }
    }

}