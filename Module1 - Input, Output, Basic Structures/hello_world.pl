;; Define namespace as main
(ns main)

;; function to provide name - not a variable
(def username "Josiah Greenwell")

;; function takes name and returns hello string
(defn hello-message
  [name]
  (str "Hello " name))
  
;; Our main function which starts the program
(defn -main
  [& args]
  (println (hello-message username)))
