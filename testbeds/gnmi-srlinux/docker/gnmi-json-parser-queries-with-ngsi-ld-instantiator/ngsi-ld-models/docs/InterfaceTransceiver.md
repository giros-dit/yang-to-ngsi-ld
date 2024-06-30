# InterfaceTransceiver

 YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceTransceiver. | [default to 'InterfaceTransceiver']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**tx_laser** | [**TxLaser**](TxLaser.md) |  | [optional] 
**oper_state** | [**InterfaceTransceiverOperState**](InterfaceTransceiverOperState.md) |  | [optional] 
**oper_down_reason** | [**InterfaceTransceiverOperDownReason**](InterfaceTransceiverOperDownReason.md) |  | [optional] 
**ddm_events** | [**DdmEvents**](DdmEvents.md) |  | [optional] 
**forward_error_correction** | [**ForwardErrorCorrection**](ForwardErrorCorrection.md) |  | [optional] 
**form_factor** | [**FormFactor**](FormFactor.md) |  | [optional] 
**functional_type** | [**FunctionalType**](FunctionalType.md) |  | [optional] 
**ethernet_pmd** | [**EthernetPmd**](EthernetPmd.md) |  | [optional] 
**connector_type** | [**ConnectorType**](ConnectorType.md) |  | [optional] 
**vendor** | [**Vendor**](Vendor.md) |  | [optional] 
**vendor_part_number** | [**InterfaceTransceiverVendorPartNumber**](InterfaceTransceiverVendorPartNumber.md) |  | [optional] 
**vendor_revision** | [**VendorRevision**](VendorRevision.md) |  | [optional] 
**vendor_lot_number** | [**VendorLotNumber**](VendorLotNumber.md) |  | [optional] 
**serial_number** | [**InterfaceTransceiverSerialNumber**](InterfaceTransceiverSerialNumber.md) |  | [optional] 
**date_code** | [**DateCode**](DateCode.md) |  | [optional] 
**fault_condition** | [**FaultCondition**](FaultCondition.md) |  | [optional] 
**wavelength** | [**InterfaceTransceiverWavelength**](InterfaceTransceiverWavelength.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_transceiver import InterfaceTransceiver

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceTransceiver from a JSON string
interface_transceiver_instance = InterfaceTransceiver.from_json(json)
# print the JSON string representation of the object
print InterfaceTransceiver.to_json()

# convert the object into a dict
interface_transceiver_dict = interface_transceiver_instance.to_dict()
# create an instance of InterfaceTransceiver from a dict
interface_transceiver_form_dict = interface_transceiver.from_dict(interface_transceiver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


