//
//  ViewController.swift
//  Threesies
//
//  Created by Carter Burns on 9/28/18.
//  Copyright © 2018 Carter Burns. All rights reserved.
//

import UIKit

class DataEntryViewController: UIViewController, UIPickerViewDataSource, UIPickerViewDelegate {

    let playerPoolArray = ["Carter","Ali","MP","RonRon","SunChow","Spidey","M1","M2","MH","Alex","Fonz","Jodie","Guest"]
    let playerPoolArray2 = ["Carter","Ali","MP","RonRon","SunChow","Spidey","M1","M2","MH","Alex","Fonz","Jodie","Guest"]
    var leftPlayerSelected = ""
    var rightPlayerSelected = ""
    var whoWon = ""
    
    // Initialize player pickers and button
    @IBOutlet weak var leftSidePlayerPicker: UIPickerView!
    @IBOutlet weak var rightSidePlayerPicker: UIPickerView!
    @IBOutlet weak var whichSideWon: UISegmentedControl!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        leftSidePlayerPicker.delegate = self
        leftSidePlayerPicker.dataSource = self
        rightSidePlayerPicker.delegate = self
        rightSidePlayerPicker.dataSource = self
    }

    // Placing UIPickerView delegate methods here, creating two TBD
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return playerPoolArray.count
        
    }
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        if pickerView.tag == 0 {
            return playerPoolArray[row]
        }
        else if pickerView.tag == 1{
            return playerPoolArray2[row]
        }
        else{
            return nil
        }
    }
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        if pickerView.tag == 0{
            leftPlayerSelected = playerPoolArray[row]
        }
        else{
            rightPlayerSelected = playerPoolArray2[row]
        }
    }

    @IBAction func gameCompleted(_ sender: UIButton) {
        if whichSideWon.selectedSegmentIndex == 0 {
            whoWon = leftPlayerSelected
        }else{
            whoWon = rightPlayerSelected
        }
        print(whoWon)
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

