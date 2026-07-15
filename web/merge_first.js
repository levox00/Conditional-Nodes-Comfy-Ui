import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "merge_first.dynamic",

    beforeRegisterNodeDef(nodeType, nodeData) {
        if (nodeData.name !== "MergeFirst") return;

        const onConnectionsChange = nodeType.prototype.onConnectionsChange;

        nodeType.prototype.onNodeCreated = function () {
            this.updateInputs();
        };

        nodeType.prototype.onConnectionsChange = function (...args) {
            if (onConnectionsChange)
                onConnectionsChange.apply(this, args);

            this.updateInputs();
        };

        nodeType.prototype.updateInputs = function () {

            // nur den ersten freien Eingang anzeigen
            let connected = 0;

            for (const input of this.inputs) {
                if (input.link != null)
                    connected++;
            }

            const wanted = Math.min(connected + 1, 64);

            while (this.inputs.length > wanted)
                this.removeInput(this.inputs.length - 1);

            while (this.inputs.length < wanted)
                this.addInput(`in_${this.inputs.length + 1}`, "*");
        };
    }
});